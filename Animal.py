from datetime import date
from MySQLHandler import MySQLHandler


class Animal:
    def __init__(
        self,
        animal_name: str,
        birth_date: str,
        sterilized: str,
        gender: str,
        species: str,
        breed: str,
        color: str,
        behavioral_warning: str,
        owner_name: str,
        email: str,
        phone: str,
        address: str,
        reg_date: str,
        med_condition: str = None,
    ):
        self.animal_id = None
        self.animal_name = animal_name
        self.birth_date = birth_date
        self.sterilized = sterilized
        self.gender = gender
        self.species = species
        self.breed = breed
        self.color = color
        self.behavioral_warning = behavioral_warning
        self.owner_name = owner_name
        self.email = email
        self.phone = phone
        self.address = address
        self.reg_date = reg_date
        self.med_condition = med_condition
        self.medical_records = []

    def add_record(self, record: str, report_date: str = None):
        if record.strip():
            if not report_date:
                report_date = date.today()
            data = [str(record), report_date]
            self.medical_records.append(data)
            add_record_to_db(self.animal_id, data)
        else:
            raise ValueError("Record field can not be empty!")

    ########## getter, setter ###########
    @property
    def medical_records(self):
        return self._medical_records

    @medical_records.setter
    def medical_records(self, medical_records):
        if isinstance(medical_records, list):
            self._medical_records = medical_records
        else:
            raise ValueError(
                "Input must be a list of dictionaries with a date and record keys!"
            )

    @property
    def animal_id(self):
        return self._animal_id

    @animal_id.setter
    def animal_id(self, animal_id: int):
        self._animal_id = animal_id

    @property
    def animal_name(self):
        return self._animal_name

    @animal_name.setter
    def animal_name(self, animal_name: str):
        self._animal_name = animal_name

    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, birth_date: str):
        self._birth_date = birth_date

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, breed: str):
        self._breed = breed

    @property
    def species(self):
        return self._species

    @species.setter
    def species(self, species: str):
        self._species = species

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color: str):
        self._color = color

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, gender: str):
        self._gender = gender

    @property
    def reg_date(self):
        return self._reg_date

    @reg_date.setter
    def reg_date(self, reg_date: str):
        self._reg_date = reg_date

    @property
    def behavioral_warning(self):
        return self._behavioral_warning

    @behavioral_warning.setter
    def behavioral_warning(self, behavioral_warning: str):
        self._behavioral_warning = behavioral_warning

    @property
    def med_condition(self):
        return self._med_condition

    @med_condition.setter
    def med_condition(self, med_condition: str):
        self._med_condition = med_condition

    @property
    def owner_name(self):
        return self._owner_name

    @owner_name.setter
    def owner_name(self, owner_name: str):
        self._owner_name = owner_name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email: str):
        self._email = email

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone: str):
        self._phone = phone

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address: str):
        self._address = address

    ########getter, setter end###########


########## Animal ##########

Animals = []


def fetch_animals():
    Animals.clear()
    try:
        mysql_handler = MySQLHandler()
        mysql_handler.connect()
        query = "select * from animals"
        data = mysql_handler.fetch_data(query)
        for row in data:
            query = "select record, rdate from record where animal_id = %s"
            value = row[0]
            records_data = mysql_handler.fetch_data(query, (value,))
            animal = Animal(
                animal_name=row[1],
                birth_date=row[2],
                sterilized=row[3],
                gender=row[4],
                species=row[5],
                breed=row[6],
                color=row[7],
                behavioral_warning=row[8],
                owner_name=row[9],
                email=row[10],
                phone=row[11],
                address=row[12],
                reg_date=row[13],
                med_condition=row[14],
            )
            animal.animal_id = int(row[0])
            animal.medical_records = records_data
            Animals.append(animal)

        mysql_handler.disconnect()
    except Exception as err:
        print(f"Error Fetching: {err}")


def add_record_to_db(animal_id: int, data):
    try:
        mysql_handler = MySQLHandler()
        mysql_handler.connect()
        query = "insert into record(animal_id, record, rdate) values(%s, %s, %s)"
        values = animal_id, data[0], data[1]
        mysql_handler.execute_query(query, values)
        mysql_handler.disconnect()
        print("New medical record added!")
    except Exception as err:
        print(f"Error inserting: {err}")

def update_animal_from_db(animal_name, birth_date,
                  sterilized, gender,
                  species, breed, color,
                  behavioral_warning, owner_name,
                  email, phone, address,
                  reg_date, med_condition, animal_id):
    try:
        mysql_handler = MySQLHandler()
        mysql_handler.connect()

        query = '''
        UPDATE animals
        SET 
        animal_name = %s,
        birth_date = %s,
        sterilized = %s,
        gender = %s,
        species = %s,
        breed = %s,
        color = %s,
        behavioral_warning = %s,
        owner_name = %s,
        email = %s,
        phone = %s,
        address = %s,
        reg_date = %s,
        med_condition = %s
        WHERE
        animal_id = %s
        '''
        values = (animal_name, birth_date,
                  sterilized, gender,
                  species, breed, color,
                  behavioral_warning, owner_name,
                  email, phone, address,
                  reg_date, med_condition, animal_id)
        mysql_handler.execute_query(query, values)
        mysql_handler.disconnect()
        print("Animal Record updated!")
    except Exception as err:
        print("Update to db failed: {err}")

def add_animal(
    animal_name: str,
    birth_date: str,
    sterilized: str,
    gender: str,
    species: str,
    breed: str,
    color: str,
    behavioral_warning: str,
    owner_name: str,
    email: str,
    phone: str,
    address: str,
    med_condition: str = None,
):
    try:
        reg_date = date.today()
        new_animal = Animal(
            animal_name,
            birth_date,
            sterilized,
            gender,
            species,
            breed,
            color,
            behavioral_warning,
            owner_name,
            email,
            phone,
            address,
            reg_date,
            med_condition,
        )
        

        query = "insert into animals (animal_name, birth_date, sterilized, gender, species, breed, color, behavioral_warning, owner_name, email, phone, address, reg_date, med_condition) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (
            animal_name,
            birth_date,
            sterilized,
            gender,
            species,
            breed,
            color,
            behavioral_warning,
            owner_name,
            email,
            phone,
            address,
            reg_date,
            med_condition,
        )
        mysql_handler = MySQLHandler()
        mysql_handler.connect()
        mysql_handler.execute_query(query, values)
        print("Entry Success!")
        new_animal.animal_id = mysql_handler.fetch_data("Select LAST_INSERT_ID()")[0][0]
        Animals.append(new_animal)
        mysql_handler.disconnect()
        return new_animal.animal_id
    except Exception as err:
        return "Entry Failed!"


def delete_record_from_db(animal_id, data):
    try:
        mysql_handler = MySQLHandler()
        mysql_handler.connect()
        query = "delete from record where animal_id=%s and record = %s and rdate = %s"
        values = animal_id, data[1], data[0]
        mysql_handler.execute_query(query, values)
        mysql_handler.disconnect()
        print("Delete Success!")
    except Exception as err:
        print(f"Delete failed: {err}")


def delete_animal_from_db(id: int):
    try:
        for animal in Animals:
            if id == animal.animal_id:
                mysql_handler = MySQLHandler()
                mysql_handler.connect()
                query = "delete from animals where animal_id = %s;"
                data = animal.animal_id
                mysql_handler.execute_query(query, (data,))
                Animals.remove(animal)
                mysql_handler.disconnect()
                print("Delete Success!")
                break
    except Exception as err:
        print(f"Error: {err}")


def main():
    an = Animal(
        "Warden",
        "june 26th 2000",
        "no",
        "alpha male",
        "wolf",
        "red wolf",
        "gray and black",
        "calm and calculative",
        "Nemo",
        "nem@gmail",
        "190238",
        "mohammadpur",
        "june 21",
        "healthy",
    )
    print(an.animal_name)


if __name__ == "__main__":
    main()
##########Animal End ##########
