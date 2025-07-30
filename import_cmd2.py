import cmd #lowercase

class Myshell(cmd.Cmd): #cmd with capital C
    prompt = 'Myshell> '  # <--this changes the (cmd) prompt

    def do_greet(self, line):
        print("hi, kausar")
    
    def do_exist(self, line):
        return True
    
Myshell().cmdloop()