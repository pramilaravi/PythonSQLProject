# Notice: no setup/teardown code needed in tests!
# The 'db' and 'db_with_data' fixtures handle everything.

def test_empty_database_with_no_users(db):
    cursor = db.cursor()
    cursor.execute('SELECT COUNT(*) as count FROM USERS')
    result = cursor.fetchone()
    assert result["count"] == 0


def test_only_active_users_returned(db_with_data):
    cursor = db_with_data.cursor()
    cursor.execute('SELECT COUNT(*) as count FROM USERS where active = 1')
    active_users = cursor.fetchall()
    assert len(active_users) == 1

def test_count_active_users(db_with_data):
    cursor = db_with_data.cursor()
    cursor.execute('SELECT COUNT(*) as count FROM USERS where active = 1')
    result = cursor.fetchone()
    

