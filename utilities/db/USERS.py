from utilities.db.db_manager import dbManager

class USERS:

    @staticmethod
    # the function checks if the email already exists in users table
    def checkIfUserExists (eMail):
        query_result = dbManager.fetch("SELECT * FROM users where email='%s'" % eMail)
        if len(query_result) == 0:
            return False
        return True

    @staticmethod
    def addUser(firstName, lastName, eMail, password):
        if USERS.checkIfUserExists(eMail):
            return False
        query_result = dbManager.commit(
            "insert into users(firstName, lastName, eMail, password) VALUES ('%s', '%s', '%s', '%s')" %
            (firstName, lastName, eMail, password))
        return query_result

    @staticmethod
    def deleteUser(eMail, password):
        if USERS.checkIfUserExists(eMail):
            user = dbManager.fetch("select * from users where eMail= ('%s') " % (eMail))
            if user[0].password == password:
                return dbManager.commit("delete from users where eMail = ('%s') " % (eMail))
            else:
                return False
        else:
            return False

    @staticmethod
    def updatePassword(eMail, lastPassword, newPassword):
        if USERS.checkIfUserExists(eMail):
            user = dbManager.fetch("select * from users where eMail= ('%s') " % (eMail))
            if user[0].password == lastPassword:
                return dbManager.commit("update users set password = ('%s') where eMail = ('%s') " % (newPassword, eMail))
            else:
                return False
        else:
            return False

    @staticmethod
    def getUser(eMail):
        if USERS.checkIfUserExists(eMail):
            return dbManager.fetch("select * from users where eMail=('%s')" % (eMail))
        else:
            return False

    @staticmethod
    def getUserFullName(eMail):
        return dbManager.fetch("SELECT CONCAT(firstName, ' ', lastName) as fullname FROM users WHERE eMail=('%s')" % (eMail))[0][0]