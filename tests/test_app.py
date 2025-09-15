import pytest
from app import create_app, db
from app.models import Task

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Task Manager" in response.data

def test_add_task(client):
    response = client.post('/add', data=dict(title="Test Task", description="Test Desc"))
    assert response.status_code == 302  # redirect after add
    with client.application.app_context():
        task = Task.query.first()
        assert task.title == "Test Task"
        assert task.status == "Pending"

def test_complete_task(client):
    with client.application.app_context():
        task = Task(title="Test Task")
        db.session.add(task)
        db.session.commit()
        task_id = task.id

    response = client.get(f'/complete/{task_id}')
    assert response.status_code == 302
    with client.application.app_context():
        task = Task.query.get(task_id)
        assert task.status == "Completed"
