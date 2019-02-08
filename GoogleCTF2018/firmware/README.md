### FIRMWARE
[Challenge Link](https://capturetheflag.withgoogle.com/?#beginners/re-firmware)

#### Getting Ready to mount image (Ubuntu)

- `$ sudo fdisk -lu ./challenge2.ext4`
- `$ sudo losetup /dev/loop0 ./challenge2.ext4`
- `$ sudo fsck -fv /dev/loop0 #error related to e2fsck` 

#### Install e2fsprogs
- `$ git clone https://github.com/tytso/e2fsprogs.git`
- `$ sudo apt install build-essential #incase you didn't install this already`
- `$ cd e2fsprogs && mkdir build && cd build`
- `$ ../configure && make && cd e2fsck && sudo make install`
- `$ sudo fsck -fv /dev/loop0`

#### Mount the image and get flag
- `$ sudo mount /dev/loop0 /mnt`
- `$ ls -al /mnt`
- `$ cp /mnt/.mediapc_backdoor_password.gz ~/tmp`
- `$ gzip -d ~/tmp/.mediapc_backdoor_password.gz`
- `$ cat ~/tmp/.mediapc_backdoor_password`

#### Cleaning Up
- `$ sudo umount /mnt`
- `$ sudo losetup -d /dev/loop0`