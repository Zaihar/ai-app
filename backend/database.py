import psycopg2

def save_chat(question,answer):
    conn = psycopg2.connect(
    host="host.docker.internal",
    database="firstDB",
    user="postgres",
    password="sanjay@1232",
    port="5432"
    )
    
    
    
    cursor = conn.cursor()
    
    cursor.execute(
    """
    INSERT INTO first (question, answer)
    VALUES (%s, %s)
    """,
    (question,answer)
    )
    conn.commit()
    cursor.close()
    conn.close()        
