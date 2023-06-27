import subprocess

def binarysearch(arr, url):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low + high) // 2
        p = arr[mid]
        command = [
            "ssh", "-p", str(p), "-o", "HostKeyAlgorithms=ssh-rsa",
            "-o", "StrictHostKeyChecking=no", url
        ]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()

        output = output.decode('utf-8')
        error = error.decode('utf-8')

        if "Lower" in output:
            print(f'[!] not this port {p}, Lower! {arr[low]} {arr[high]}')
            low = mid + 1
        elif "Higher" in output:
            print(f'[!] not this port {p}, Higher! {arr[low]} {arr[high]}')
            high = mid - 1
        else:
            print(f'This port {p}')
            break
            
arr  = [i for i in range(9000,13450)]
print(len(arr))

binarysearch(arr, "10.10.229.28")
