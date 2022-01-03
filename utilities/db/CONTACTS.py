from utilities.db.db_manager import dbManager

class CONTACTS:

    @staticmethod
    def addContact(firstName, lastName, eMail, content):
        query_result = dbManager.commit(
            "insert into contacts(firstName, lastName, eMail, content) VALUES ('%s', '%s', '%s', '%s')" %
            (firstName, lastName, eMail, content))
        return query_result




