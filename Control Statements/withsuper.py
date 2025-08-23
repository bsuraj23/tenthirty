class Child(Parent):
    def action(self):
        print("Child: Performing child-specific action")
        super().action()
        super().action()  # Called again
        print("Child: Finished calling parent action")