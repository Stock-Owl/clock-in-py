from datetime import datetime as dt
from datetime import timedelta as tdelta
from os.path import dirname
from os import getcwd as gwd
from re import findall

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

#TODO: sum func etc.

class Log:
    """
    I should write a class description here... hehehe
    """
    def __init__(self,
                 user: str = "",
                 project: str = "",
                 log_type: str = "LOG",
                 state: str = "",
                 log_path: str = "./tlog/",
                 log_filename: str = ""):

        """
        Initializes a Log object all values are set to 'N/A' unless
        specified in arguments of the initializer except path and filename
        """

        self.user: str = "N/A" if user == "" else user
        self.state: str = "N/A" if state == "" else state
        self.project: str = "N/A" if project == "" else project
        # self.log_type has a default
        self.log_type: str = log_type
        # self.log_path has a default
        self.log_path: str = log_path
        self.log_filename: str = f"{dt.now().strftime(r'%Y-%m-%d')}.tlog" \
            if log_filename == "" else f"{log_filename}.tlog"
        # NOT a class attribute (because fuck you, that's why)
        full_path: str = f"{self.log_path}/{self.log_filename}"

        with open(full_path, mode = 'w+', encoding = "utf-8") as f:
            pass
    def t_sum():
        ...

    def l_sum(self, path: str = "") -> tuple[tuple[str, dt], ...]:
        """Sums up hours logged by each user and returns a 2d tuple storing the sums and users in pairs (tuple(tuple))
        
        Requires a path to the *.tlog file"""

        if path == "": path = f"{self.log_path}/{self.log_filename}"
        print(path)
        # sum_ stores the summed times of useres. Each user's time is stored independetnly
        # (hence: tuple(tuple)), first: user second: summed time
        sum_: tuple[tuple[str, dt], ...]
        with open(path, mode = 'r+', encoding='utf-8') as f:
            for line in f:
                print(line, end="")
                line = line.strip('[]')
                dirs: list[str] = findall("\[[^]]*\]", line)
                # TODO: sum shit up, create dt objects ()
                # add log format specifiers


    def s_time(self,   
                time_format: str = r"%Y-%%d %H:%M:",
                display_format: str = "{} — {}",
                range_end: dt | str = dt.now()) -> str:
        
        if isinstance(range_end, str):
            range_end = dt(range_end)
        now: dt = dt.now()

        """
        this is the fun part
        compares the strings, since datetime object attributes are read only
        therefore it doesn't compare on a microsecond level
        unless specified in time_format
        for some dumb ass reason the 'resolution' attribute
        is read-only too so this is what I hat to resort to
        """

        if now.strftime(time_format) != range_end.strftime(time_format):
            timerange = display_format.format(
                now.strftime(time_format),
                range_end.strftime(time_format))
            return timerange
        return now.strftime(time_format)

    def mk_log_line(self, log_type: str = "", state: str = "", user: str = "", project: str = "", t_format: str = r"%H:%M") ->  str:
        """generates a log line from given arguments in pre-defined format or using properties given at initialization"""
        if log_type == "": log_type = self.log_type 
        if state == "": state = self.state
        if user == "": user = self.user
        if project == "": project = self.project
    #
        cwd_dir: str = gwd()
        time_: str = self.s_time(time_format = t_format)
        log_line: str = f"[{log_type}][{state}][{time_}]\t[{user}]/[{project}]@[{cwd_dir}]\n"
        return log_line

    def log(self, path: str = "", filename = "", log_line: str = ""):
        """writes log line into specifies .tlog file. Makes a log line if none is given"""
        if path == "":
            path = self.log_path    #defaults to predefined path './tlog/'
        if filename == "":
            filename = self.log_filename    #defaults to predefined filename '[current date].tlog'
        if log_line == "":
            log_line = self.mk_log_line(self.log_type, self.state, self.user, self.project)
        full_path = f"{path}/{filename}"
        with open(full_path, mode = "a+", encoding = "utf8") as f:
            f.write(log_line)

    def __str__(self):
        """returns a nicely formatted string version of the object's properties"""

        return f"—————\nLog class object\nprops:\n\t>user: {self.user}\n\t>state: {self.state}\n\t>project: {self.project}\n\t>tpye: {self.log_type}\n\t@ {gwd()}\n—————"
