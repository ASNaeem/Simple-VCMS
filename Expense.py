from MySQLHandler import MySQLHandler


class Expense:
    def __init__(
        self,
        issuer_id: int,
        handler_id: int,
        expense_date: str,
        handle_date: str,
        amount: float,
        justification: str,
    ):
        self.expense_id = None
        self.issuer_id = issuer_id
        self.handler_id = handler_id
        self.expense_date = expense_date
        self.handle_date = handle_date
        self.amount = amount
        self.justification = justification

    ############## getter, setter ###########
    @property
    def expense_id(self):
        return self._expense_id

    @expense_id.setter
    def expense_id(self, expense_id: int):
        self._expense_id = expense_id

    @property
    def issuer_id(self):
        return self._issuer_id

    @issuer_id.setter
    def issuer_id(self, issuer_id: int):
        self._issuer_id = issuer_id

    @property
    def handler_id(self):
        return self._handler_id

    @handler_id.setter
    def handler_id(self, handler_id: int):
        self._handler_id = handler_id

    @property
    def expense_date(self):
        return self._expense_date

    @expense_date.setter
    def expense_date(self, expense_date: str):
        self._expense_date = expense_date

    @property
    def handle_date(self):
        return self._handle_date

    @handle_date.setter
    def handle_date(self, handle_date: str):
        self._handle_date = handle_date

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount: float):
        self._amount = amount

    @property
    def justification(self):
        return self._justification

    @justification.setter
    def justification(self, justification: str):
        self._justification = justification

    ############## getter, setter ###########


############### expenses operations ################

Expenses = []


def fetch_expenses():
    try:
        mysql_handler = MySQLHandler()
        mysql_handler.connect()
        query = "select * from expenses;"
        data = mysql_handler.fetch_data(query)
        for row in data:
            expense = Expense(
                issuer_id=row[1],
                handler_id=row[2],
                expense_date=str(row[3]),
                handle_date=str(row[4]),
                amount=float(row[5]),
                justification=row[6],
            )
            expense.expense_id = int(row[0])
            Expenses.append(expense)
        # print("after for loop tesing")
        mysql_handler.disconnect()

    except Exception as err:
        print(f"Error Fetching: {err}")


def add_expense(
    issuer_id: int,
    handler_id: int,
    expense_date: str,
    handle_date: str,
    amount: float,
    justification: str,
):
    try:
        new_expense = Expense(
            issuer_id, handler_id, expense_date, amount, justification
        )
        Expenses.append(new_expense)

        query = "insert into expenses (handler_id, expense_date, handle_date, amount, justification) values (%S, %s, %s, %s, %s);"
        data = values(handler_id, expense_date, handle_date, amount, justification)

        mysql_handler = MySQLHandler()
        mysql_handler.connect()
        mysql_handler.execute_query(query, data)
        mysql_handler.disconnect()
        print("Entry Success!")
    except Exception as err:
        print(f"Entry Failed: {err}")


def delete_expenses(id: int):
    try:
        for expense in Expenses:
            if id == expense.expense_id:
                mysql_handler = MySQLHandler()
                mysql_handler.connect()
                query = "delete from expenses where expense_id = %s;"
                data = id
                mysql_handler.execute_query(query, (data,))
                Expenses.remove(expense)
                mysql_handler.disconnect()
                print("Delete Success!")
                break
    except Exception as err:
        print(f"Error: {err}")


def update_expense_to_db(
    self,
    expense_id: int,
    issuer_id: int,
    handler_id: int,
    expense_date_obj: str,
    handle_date_obj: str,
    amount: float,
    justification: str,
):
    try:
        mysql_handler = MySQLHandler()
        mysql_handler.connect()

        query = "UPDATE expenses SET  handler_id = %s, issuer_id = %s, expense_date = %s, handler_date = %s, amount = %s, justification = %s where expense_id = %s;"
        values = (
            handler_id,
            issuer_id,
            expense_date_obj,
            handle_date_obj,
            amount,
            justification,
        )
        mysql_handler.execute_query(querry, values)
        mysql_handler.disconnect()
        print("Expense Information Updated!")

    except Exception as err:
        print(f"Expense Update Failed: {err}")
