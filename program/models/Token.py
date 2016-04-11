class Token(object):
    def is_circle(self):
        return False

    def is_cross(self):
        return False

    def is_equal(self, token):
        return False

    def is_empty(self):
        return False


class Cross(Token):
    def is_cross(self):
        return True

    def is_equal(self,token):
        return token.is_cross()


class Circle(Token):
    def is_circle(self):
        return True

    def is_equal(self,token):
        return token.is_circle()


class EmptyToken(Token):

    def is_empty(self):
        return True