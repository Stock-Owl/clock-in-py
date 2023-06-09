from datetime import datetime as dt
from datetime import timedelta as tdelta
from os.path import dirname
from os import getcwd as gwd

"""
%a	Weekday, short version	Wed	
%A	Weekday, full version	Wednesday	
%w	Weekday as a number 0-6, 0 is Sunday	3	
%d	Day of month 01-31	31	
%b	Month name, short version	Dec	
%B	Month name, full version	December	
%m	Month as a number 01-12	12	
%y	Year, short version, without century	18	
%Y	Year, full version	2018	
%H	Hour 00-23	17	
%I	Hour 00-12	05	
%p	AM/PM	PM
%M	Minute 00-59	41	
%S	Second 00-59	08	
%f	Microsecond 000000-999999	548513	
%z	UTC offset	+0100	
%Z	Timezone	CST	
%j	Day number of year 001-366	365	
%U	Week number of year, Sunday as the first day of week, 00-53	52	
%W	Week number of year, Monday as the first day of week, 00-53	52	
%c	Local version of date and time	Mon Dec 31 17:41:00 2018	
%C	Century	20	
%x	Local version of date	12/31/18	
%X	Local version of time	17:41:00	
%%	A % character	%	
%G	ISO 8601 year	2018	
%u	ISO 8601 weekday (1-7)	1	
%V	ISO 8601 weeknumber (01-53)	01
"""                                                                                            

class Log:
    """
    I should write a class description here... hehehe
    """
    def __init__(self,
                 user: str = "",
                 project: str = "",
                 log_type: str = "LOG",
                 state: str = "",
                 log_path: str = "./tlog/"):

        """Initializes a Log object all values are set to N/A unless specified in arguments of the initializer"""

        self.user: str = "N/A" if user == "" else user
        self.state: str = "N/A" if state == "" else state
        self.project: str = "N/A" if project == "" else project
        # self.log_type has a default
        self.log_type: str = log_type
        # self.log_path has a default
        self.log_path: str = log_path

    def s_time(time_format: str = '%Y-%d %H:%M:',
               display_format: str = "{} — {}",
               range_end: dt | str = dt.now()) -> str:
        if isinstance(range_end, str):
            range_end = dt(range_end)
        now: dt = dt.now()
        now.microsecond = 0
        range_end.microsecond = 0
        if now != range_end:
            timerange = display_format.format(
                now.strftime(time_format),
                range_end.strftime(time_format))
            return timerange
        return now.strftime(time_format)

    def mk_log_line(self, log_type: str = "", state: str = "", user: str = "", project: str = "", t_format: str = "%H:%M") ->  None:
        """generates a log line from given arguments in pre-defined format or using properties given at initialization"""
        if log_type == "": log_type = self.log_type 
        if state == "": state = self.state
        if user == "": user = self.user
        if project == "": project = self.project
    #
        cwd_dir: str = gwd()
        time_:str = self.s_time(format = t_format)
        log_line: str = f"[{log_type}][{state}][{time_}][{user}]/[{project}]@[{cwd_dir}]\n"
        return log_line

    def log(self, path: str = "", log_line: str = ""):
        """writes log line into specifies .tlog file. Makes a log line if none is given"""
        if path == "":
            path = self.log_path        #defaults to predefined path './tlog/'
        if log_line == "":
            log_line = self.mk_log_line(self.log_type, self.state, self.user, self.project)
        with open(path, mode = "a+", encoding = "utf8") as f:
            f.write(log_line + "\n")

    def __str__(self):
        """returns a nicely formatted string version of the object's properties"""

        return f"—————\nLog class object\nprops:\n\t>user: {self.user}\n\t>state: {self.state}\n\t>project: {self.project}\n\t>tpye: {self.log_type}\n\t@ {gwd()}\n—————"

mylog = Log("me", "this project")
print(mylog.mklogline())