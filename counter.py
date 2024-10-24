class Counter:
    def __init__(self):
        self.count = 0
        self.flag_is_body = False

    def __enter__(self):
        self.flag_is_body = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.flag_is_body = False

    def add(self):
        if self.flag_is_body:
            self.count += 1
        else:
            raise Exception("Счетчик задан вне тела try")
        return f'счетчик равен {self.count}'
