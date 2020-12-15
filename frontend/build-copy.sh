npm run build &&
rsync -rcv build/* /mnt/raid-0/docker/swag/config/www/neetcode-signals/ --delete