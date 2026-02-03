"""
Dashboard Data Generator
Creates JSON data files for HTML dashboards from database analysis
"""

import sqlite3
import json
from pathlib import Path
from datetime import datetime

DB_PATH = Path(__file__).parent.parent / "data" / "player_analytics.db"
OUTPUT_DIR = Path(__file__).parent.parent / "dashboards" / "assets"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def get_segment_overview_data(conn):
    """Generate segment overview data"""
    cursor = conn.cursor()
    
    # Persona distribution
    cursor.execute("""
        SELECT persona, COUNT(*) as count, 
               ROUND(AVG(lifetime_value), 2) as avg_ltv,
               ROUND(SUM(lifetime_value), 2) as total_ltv
        FROM v_persona_assignment
        GROUP BY persona
        ORDER BY count DESC
    """)
    personas = [
        {"name": row[0], "count": row[1], "avgLtv": row[2], "totalLtv": row[3]}
        for row in cursor.fetchall()
    ]
    
    # Engagement levels
    cursor.execute("""
        SELECT engagement_level, COUNT(*) as count
        FROM v_engagement_segments
        GROUP BY engagement_level
    """)
    engagement = [{"level": row[0], "count": row[1]} for row in cursor.fetchall()]
    
    # Monetization tiers
    cursor.execute("""
        SELECT monetization_tier, COUNT(*) as count, 
               ROUND(SUM(lifetime_value), 2) as revenue
        FROM v_monetization_segments
        GROUP BY monetization_tier
    """)
    monetization = [
        {"tier": row[0], "count": row[1], "revenue": row[2]}
        for row in cursor.fetchall()
    ]
    
    # RFM segments
    cursor.execute("""
        SELECT rfm_segment, COUNT(*) as count, action_priority
        FROM v_rfm_segments
        GROUP BY rfm_segment, action_priority
        ORDER BY count DESC
    """)
    rfm = [
        {"segment": row[0], "count": row[1], "priority": row[2]}
        for row in cursor.fetchall()
    ]
    
    # Platform distribution
    cursor.execute("""
        SELECT platform, COUNT(*) as count, 
               ROUND(AVG(lifetime_value), 2) as avg_ltv
        FROM players
        GROUP BY platform
    """)
    platforms = [
        {"platform": row[0], "count": row[1], "avgLtv": row[2]}
        for row in cursor.fetchall()
    ]
    
    # KPI summary
    cursor.execute("""
        SELECT 
            COUNT(*) as total_players,
            SUM(CASE WHEN account_status = 'active' THEN 1 ELSE 0 END) as active_players,
            ROUND(SUM(lifetime_value), 2) as total_revenue,
            ROUND(AVG(lifetime_value), 2) as avg_ltv,
            ROUND(AVG(total_playtime_hours), 1) as avg_playtime
        FROM players
    """)
    kpi = cursor.fetchone()
    
    return {
        "personas": personas,
        "engagement": engagement,
        "monetization": monetization,
        "rfm": rfm,
        "platforms": platforms,
        "kpi": {
            "totalPlayers": kpi[0],
            "activePlayers": kpi[1],
            "totalRevenue": kpi[2],
            "avgLtv": kpi[3],
            "avgPlaytime": kpi[4]
        },
        "generatedAt": datetime.now().isoformat()
    }


def get_persona_deepdive_data(conn):
    """Generate persona deep-dive data"""
    cursor = conn.cursor()
    
    personas_data = {}
    
    cursor.execute("SELECT DISTINCT persona FROM v_persona_assignment")
    personas = [row[0] for row in cursor.fetchall()]
    
    for persona in personas:
        # Basic stats
        cursor.execute("""
            SELECT 
                COUNT(*) as population,
                ROUND(AVG(total_playtime_hours), 1) as avg_playtime,
                ROUND(AVG(lifetime_value), 2) as avg_ltv,
                ROUND(AVG(avg_session_duration), 1) as avg_session,
                ROUND(AVG(pvp_ratio) * 100, 1) as pvp_pct,
                ROUND(AVG(social_score), 2) as social_score,
                ROUND(SUM(lifetime_value), 2) as total_revenue
            FROM v_persona_assignment
            WHERE persona = ?
        """, (persona,))
        stats = cursor.fetchone()
        
        # Platform breakdown
        cursor.execute("""
            SELECT p.platform, COUNT(*) as count
            FROM v_persona_assignment pa
            JOIN players p ON pa.player_id = p.player_id
            WHERE pa.persona = ?
            GROUP BY p.platform
        """, (persona,))
        platforms = [{"platform": row[0], "count": row[1]} for row in cursor.fetchall()]
        
        # Game mode preferences
        cursor.execute("""
            SELECT ps.game_mode, COUNT(*) as count
            FROM v_persona_assignment pa
            JOIN player_sessions ps ON pa.player_id = ps.player_id
            WHERE pa.persona = ?
            GROUP BY ps.game_mode
            ORDER BY count DESC
            LIMIT 5
        """, (persona,))
        game_modes = [{"mode": row[0], "count": row[1]} for row in cursor.fetchall()]
        
        personas_data[persona] = {
            "population": stats[0],
            "avgPlaytime": stats[1],
            "avgLtv": stats[2],
            "avgSession": stats[3],
            "pvpPct": stats[4],
            "socialScore": stats[5],
            "totalRevenue": stats[6],
            "platforms": platforms,
            "gameModes": game_modes
        }
    
    return {"personas": personas_data, "generatedAt": datetime.now().isoformat()}


def get_performance_data(conn):
    """Generate performance comparison data"""
    cursor = conn.cursor()
    
    # Persona comparison matrix
    cursor.execute("""
        SELECT 
            persona,
            COUNT(*) as population,
            ROUND(AVG(total_playtime_hours), 1) as avg_playtime,
            ROUND(AVG(lifetime_value), 2) as avg_ltv,
            ROUND(AVG(avg_session_duration), 1) as avg_session,
            ROUND(AVG(pvp_ratio) * 100, 1) as pvp_pct,
            ROUND(AVG(social_score), 2) as social_score,
            ROUND(AVG(total_achievements), 0) as avg_achievements
        FROM v_persona_assignment
        GROUP BY persona
    """)
    
    personas = []
    for row in cursor.fetchall():
        personas.append({
            "name": row[0],
            "population": row[1],
            "playtime": row[2],
            "ltv": row[3],
            "session": row[4],
            "pvp": row[5],
            "social": row[6],
            "achievements": row[7]
        })
    
    # Revenue by persona
    cursor.execute("""
        SELECT persona, ROUND(SUM(lifetime_value), 2) as revenue
        FROM v_persona_assignment
        GROUP BY persona
        ORDER BY revenue DESC
    """)
    revenue = [{"persona": row[0], "revenue": row[1]} for row in cursor.fetchall()]
    
    return {
        "personas": personas,
        "revenue": revenue,
        "generatedAt": datetime.now().isoformat()
    }


def main():
    print("Generating dashboard data...")
    conn = sqlite3.connect(DB_PATH)
    
    # Generate all data files
    overview_data = get_segment_overview_data(conn)
    with open(OUTPUT_DIR / "segment_overview.json", 'w') as f:
        json.dump(overview_data, f, indent=2)
    print(f"  Generated segment_overview.json")
    
    deepdive_data = get_persona_deepdive_data(conn)
    with open(OUTPUT_DIR / "persona_deepdive.json", 'w') as f:
        json.dump(deepdive_data, f, indent=2)
    print(f"  Generated persona_deepdive.json")
    
    performance_data = get_performance_data(conn)
    with open(OUTPUT_DIR / "performance_comparison.json", 'w') as f:
        json.dump(performance_data, f, indent=2)
    print(f"  Generated performance_comparison.json")
    
    conn.close()
    print(f"\nDashboard data saved to: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
