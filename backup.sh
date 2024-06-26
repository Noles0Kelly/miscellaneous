#!/bin/bash

# Variables
SOURCE_DIR="/path/to/source"   # Replace with the directory you want to backup
BACKUP_DIR="/path/to/backup"   # Replace with the directory where backups should be stored
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
DEST_DIR="${BACKUP_DIR}/backup_${TIMESTAMP}"

# Create backup directory if it doesn't exist
mkdir -p "$BACKUP_DIR"

# Copy files from source to destination
cp -r "$SOURCE_DIR" "$DEST_DIR"

# Provide feedback to the user
if [ $? -eq 0 ]; then
  echo "Backup successful! Files copied to $DEST_DIR"
else
  echo "Backup failed!"
fi
