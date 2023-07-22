import json
import pytest

from Homework_14.project import Project, User, AccessException, LevelException


@pytest.fixture
def dict_users():
    return {
        "1": {"123": "Иван", "741": "Наталья"},
        "2": {"456": "Антон", "258": "Ирина"},
        "3": {"789": "Александр", "852": "Михаил"},
        "4": {"321": "Андрей", "369": "Леонид"},
        "5": {"654": "Григорий", "963": "Николай"},
        "6": {"987": "Ольга", "359": "Алексей"},
        "7": {"147": "Сергей", "751": "Тимофей"}
    }


@pytest.fixture
def file_users(dict_users, tmp_path):
    f_name = tmp_path / 'test_users.json'
    with open(f_name, 'w', encoding='utf-8') as f:
        json.dump(dict_users, f, indent=2, ensure_ascii=False)

    yield f_name
    f_name.unlink()


@pytest.fixture
def get_project():
    return Project([User("123", "Иван", "1"), User("741", "Наталья", "1"), User("456", "Антон", "2"),
                    User("258", "Ирина", "2"), User("789", "Александр", "3"), User("852", "Михаил", "3"),
                    User("321", "Андрей", "4"), User("369", "Леонид", "4"), User("654", "Григорий", "5"),
                    User("963", "Николай", "5"), User("987", "Ольга", "6"), User("359", "Алексей", "6"),
                    User("147", "Сергей", "7"), User("751", "Тимофей", "7")])


@pytest.fixture
def get_login_project(get_project):
    get_project.login("369", "Леонид")
    return get_project


def test_create_project_from_json_file(file_users, get_project):
    assert Project.from_json_file(file_users) == get_project


def test_login_exception(get_project):
    with pytest.raises(AccessException):
        get_project.login('999', "Игорь")


def test_login(get_login_project):
    assert User("369", "Леонид", "4") == get_login_project.admin


def test_add_user_exception(get_login_project):
    with pytest.raises(LevelException):
        get_login_project.add_user('777', 'Антон', '2')


def test_add_user(get_login_project):
    get_login_project.add_user('999', 'Степан', '6')
    assert User('999', 'Степан', '6') in get_login_project


def test_remove_user_exception(get_login_project):
    with pytest.raises(LevelException):
        get_login_project.remove_user('456')


def test_remove_user(get_login_project):
    get_login_project.remove_user('359')
    assert User("359", "Алексей", "6") not in get_login_project
