from fcntl import ioctl

class IOCTL:
  def __init__(self, base, device_path):
    self.base = base
    self.device_path = device_path

  def send_command(self, cmd):
    with open(self.device_path) as fh:
      full_cmd = ord(self.base) << (4*2) | cmd
      res = ioctl(fh, full_cmd, 0)
    return res

  
