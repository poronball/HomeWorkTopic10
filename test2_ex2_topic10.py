import pytest


@pytest.fixture
def developer_fixture():
    def init_developer(seniority):
        return Developer(name = 'bob', seniority=seniority)

    return init_developer


@pytest.mark.parametrize('enter,exception', [(1, 1), (5, 2), (8, 3), (13, 4)])
def test_developer_method(developer_fixture, enter, exception):
    dev_func_testing = developer_fixture(2)
    for i in range(enter):
        dev_func_testing.check_if_it_is_time_for_upgrade()
    assert dev_func_testing.grade == exception


@pytest.fixture
def designer_fixture():
    def init_designer(seniority):
        return Designer(name = 'Boba', seniority=seniority, awards = 2)

    return init_designer


@pytest.mark.parametrize('enter,exception', [(1, 1), (5, 2), (15, 3), (20, 4)])
def test_designer_metod(designer_fixture, enter, exception):
    design_func_testing = designer_fixture(2)
    for i in range(enter):
        design_func_testing.check_if_it_is_time_for_upgrade()
    assert design_func_testing.grade == exception


class Employee:
    def __init__(self, name, seniority, awards):
        self.name = name
        self.seniority = seniority
        self.awards = awards

        self.grade = 1

    def grade_up(self):
        """Повышает уровень сотрудника"""
        self.grade += 1

    def publish_grade(self):
        """Публикация результатов аккредитации сотрудников"""
        print(self.name, self.grade)


class Developer(Employee):
    def __init__(self, name, seniority, awards=0):
        super().__init__(name, seniority, awards=0)

    def check_if_it_is_time_for_upgrade(self):
        # для каждой аккредитации увеличиваем счетчик на 1
        # пока считаем, что все разработчики проходят аккредитацию
        self.seniority += 1

        # условие повышения сотрудника из презентации
        if self.seniority % 5 == 0:
            self.grade_up()

        # публикация результатов
        return self.publish_grade()


class Designer(Employee):
    def __init__(self, name, seniority, awards):
        super().__init__(name, seniority, awards)

    def check_if_it_is_time_for_upgrade(self):
        if self.seniority == 0:
            self.seniority = 1 + self.awards * 2
        else:
            self.seniority += 1
        if self.seniority % 7 == 0:
            self.grade_up()

        return self.publish_grade()
