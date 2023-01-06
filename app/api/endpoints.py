from typing import Optional

from app.schemas.schemas import EducationLevel, Person
from fastapi import APIRouter, Body, Path, Query

# Создаём объект роутера.
router = APIRouter()


# Меняем метод GET на POST, указываем статичный адрес.
@router.post('/hello')
# Вместо множества параметра теперь будет только один - person,
# в качестве аннотации указываем класс Person.
def post_greetings(
        person: Person = Body(
            ..., examples=Person.Config.schema_extra['examples']
        )
) -> dict[str, str]:
    # Обращение к атрибутам класса происходит через точку;
    # при этом будут работать проверки на уровне типов данных.
    # В IDE будут работать автодополнения.
    if isinstance(person.surname, list):
        surnames = ' '.join(person.surname)
    else:
        surnames = person.surname
    result = ' '.join([person.name, surnames])
    result = result.title()
    if person.age is not None:
        result += ', ' + str(person.age)
    if person.education_level is not None:
        result += ', ' + person.education_level.lower()
    if person.is_staff:
        result += ', сотрудник'
    return {'Hello': result}


@router.get(
    '/{name}',
    tags=['common methods'],
    summary='Общее приветствие',
    response_description='Полная строка приветствия'
)
def get_greetings(
        *,
        # У параметров запроса name и surname значений по умолчанию нет,
        # поэтому в первый параметр ставим многоточие, Ellipsis.
        name: str = Path(
            ..., min_length=2, max_length=20,
            title='Полное имя', description='Можно вводить в любом регистре'
        ),
        surname: list[str] = Query(..., min_length=2, max_length=50),
        # gt означает "больше", le — "меньше".
        age: Optional[int] = Query(None, ge=5, le=99),
        is_staff: bool = Query(
            False, alias='is-staff', include_in_schema=False
        ),
        education_level: Optional[EducationLevel] = None,
) -> dict[str, str]:
    """
    Приветствие пользователя:

    - **name**: имя
    - **surname**: фамилия
    - **age**: возраст (опционально)
    - **education_level**: уровень образования (опционально)
    """
    surnames = ' '.join(surname)
    result = ' '.join([name, surnames])
    result = result.title()
    if age is not None:
        result += ', ' + str(age)
    if education_level is not None:
        result += ', ' + education_level.lower()
    if is_staff:
        result += ', сотрудник'
    return {'Hello': result}
