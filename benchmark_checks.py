import subprocess

def check_cramfs_disabled():
    try:
        result = subprocess.run(['lsmod'], capture_output=True, text=True)
        if 'cramfs' in result.stdout:
            return False, "cramfs filesystem is enabled"
        return True, "cramfs filesystem is disabled"
    except Exception as e:
        return False, str(e)

def check_squashfs_disabled():
    try:
        result = subprocess.run(['lsmod'], capture_output=True, text=True)
        if 'squashfs' in result.stdout:
            return False, "squashfs filesystem is enabled"
        return True, "squashfs filesystem is disabled"
    except Exception as e:
        return False, str(e)

def check_udf_disabled():
    try:
        result = subprocess.run(['lsmod'], capture_output=True, text=True)
        if 'udf' in result.stdout:
            return False, "udf filesystem is enabled"
        return True, "udf filesystem is disabled"
    except Exception as e:
        return False, str(e)

def check_tmp_configured():
    try:
        with open('/etc/fstab', 'r') as f:
            content = f.read()
            if 'tmpfs' in content:
                return True, "/tmp is configured"
            else:
                return False, "/tmp is not configured"
    except Exception as e:
        return False, str(e)

def check_nodev_on_tmp():
    try:
        result = subprocess.run(['mount'], capture_output=True, text=True)
        if '/tmp' in result.stdout and 'nodev' in result.stdout:
            return True, "nodev option is set on /tmp partition"
        return False, "nodev option is not set on /tmp partition"
    except Exception as e:
        return False, str(e)

# Function to dynamically add checks
def dynamic_check(command, check_string, success_message, failure_message):
    try:
        result = subprocess.run(command, capture_output=True, text=True)
        if check_string in result.stdout:
            return True, success_message
        return False, failure_message
    except Exception as e:
        return False, str(e)

def check_service_running(service_name):
    try:
        result = subprocess.run(['systemctl', 'is-active', service_name], capture_output=True, text=True)
        if 'active' in result.stdout:
            return True, f"{service_name} is running"
        return False, f"{service_name} is not running"
    except Exception as e:
        return False, str(e)

# Add more check functions as needed based on the rules in the CSV
