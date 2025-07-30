import cmd

class My(cmd.Cmd):
    def do_greet(self, arg):
        """Greet the user."""
        print(f"Hello, {arg}!")
    
    def do_exit(self, arg):
        """Exit the command line interface."""
        print("Goodbye!")
        return True
My().cmdloop()  # Start the command loop