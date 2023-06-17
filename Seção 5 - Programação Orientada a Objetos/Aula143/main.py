from log import LogFileMixin, LogPrintMixin

lp = LogPrintMixin()
lp.log_error('qualquer coisa')
lp.log_success('Que Legal')
lp = LogFileMixin()
lp.log_error('Qualquer coisa')
lp.log_sucess("Que legal")