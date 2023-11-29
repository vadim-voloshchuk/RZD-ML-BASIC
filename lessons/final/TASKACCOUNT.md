Давайте рассмотрим задачу для ООП банка. Допустим, у нас есть базовый класс `Account`, представляющий банковский счет, и два подкласса: `SavingsAccount` (сберегательный счет) и `CheckingAccount` (расчетный счет). Вот задача:

### Задача:

#### Класс `Account`:
1. Реализовать класс `Account` с атрибутами:
   - `account_number` (номер счета)
   - `holder_name` (имя владельца)
   - `balance` (баланс)

2. Реализовать методы:
   - `__init__`: конструктор, который инициализирует атрибуты класса.
   - `deposit(amount)`: метод для внесения средств на счет.
   - `withdraw(amount)`: метод для снятия средств со счета.
   - `get_balance()`: метод для получения текущего баланса.

#### Подкласс `SavingsAccount`:
1. Создать подкласс `SavingsAccount`, который наследует от класса `Account`.
2. Реализовать метод `calculate_interest()`, который добавляет к балансу проценты (допустим, 5% годовых).

#### Подкласс `CheckingAccount`:
1. Создать подкласс `CheckingAccount`, который также наследует от класса `Account`.
2. Реализовать метод `deduct_fees()`, который вычитает комиссию за обслуживание (допустим, 1% от баланса ежемесячно).

#### Пример использования:

```python
# Создаем экземпляр сберегательного счета
savings_account = SavingsAccount("123456789", "John Doe", 1000)

# Вносим средства и получаем баланс
savings_account.deposit(500)
print("Current balance:", savings_account.get_balance())

# Рассчитываем проценты и получаем баланс после начисления процентов
savings_account.calculate_interest()
print("Balance after interest:", savings_account.get_balance())

# Создаем экземпляр расчетного счета
checking_account = CheckingAccount("987654321", "Jane Doe", 2000)

# Вносим средства и получаем баланс
checking_account.deposit(1000)
print("Current balance:", checking_account.get_balance())

# Вычитаем комиссию за обслуживание и получаем баланс после вычета комиссии
checking_account.deduct_fees()
print("Balance after fees:", checking_account.get_balance())
```

Эта задача позволит вам применить основные принципы ООП, такие как наследование и инкапсуляция, для моделирования банковских счетов с различным поведением.