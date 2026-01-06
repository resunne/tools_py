log_ordered_params: list[str] = [
    'request',
    'status',
    'time_local',
    'remote_addr',
    'remote_user',
    'body_bytes_sent',
    'http_referer',
    'http_user_agent',
    'http_x_forwarded_for'
]


def gen_log_str() -> str:
    log_str: str = ''
    param_max_len: int = len(max(log_ordered_params, key=lambda param: len(param.strip()), default=''))
    for param in log_ordered_params:
        log_str += rf'{(param := param.strip()).rjust(param_max_len, ' ')}: ${param}\r\n'
    log_str += r'\r\n'
    return log_str


if __name__ == '__main__':
    print(gen_log_str())
