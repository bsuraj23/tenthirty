import cmd

class myshell(cmd.cmd):
    def do_greet(self,line):
        print("hi,",line)

        def do_exist(self,line):
            return True
        myshell().cmdloop()