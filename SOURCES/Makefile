
CFLAGS := -Wall -g -I/opt/cpanel/ea-openssl11/include -I/usr/include -I. -DSIZEOF_OFF_T=8 -DHAVE_FSEEKO=1 -DHAVE_FTELLO=1 -DHAVE_OPENSSL -DHAVE_SECURE_RANDOM=1 -fPIC
DEFS := $(DEFS)
CC := gcc $(CFLAGS) $(INC) $(DEFS)
LDFLAGS := -lc -lm -lbz2 -lz -llzma -L/opt/cpanel/ea-openssl11/lib -lcrypto -lssl

HEADERS = \
    compat.h \
    zip_crypto_commoncrypto.h \
    zip_crypto_gnutls.h \
    zip_crypto.h \
    zip_crypto_mbedtls.h \
    zip_crypto_openssl.h \
    zip.h \
    zipint.h \

OBJS = \
    zip_add.o \
    zip_add_dir.o \
    zip_add_entry.o \
    zip_algorithm_bzip2.o \
    zip_algorithm_deflate.o \
    zip_algorithm_xz.o \
    zip_buffer.o \
    zip_close.o \
    zip_crypto_openssl.o \
    zip_delete.o \
    zip_dir_add.o \
    zip_dirent.o \
    zip_discard.o \
    zip_entry.o \
    zip_error.o \
    zip_error_clear.o \
    zip_error_get.o \
    zip_error_get_sys_type.o \
    zip_error_strerror.o \
    zip_error_to_str.o \
    zip_err_str.o \
    zip_extra_field_api.o \
    zip_extra_field.o \
    zip_fclose.o \
    zip_fdopen.o \
    zip_file_add.o \
    zip_file_error_clear.o \
    zip_file_error_get.o \
    zip_file_get_comment.o \
    zip_file_get_external_attributes.o \
    zip_file_get_offset.o \
    zip_filerange_crc.o \
    zip_file_rename.o \
    zip_file_replace.o \
    zip_file_set_comment.o \
    zip_file_set_encryption.o \
    zip_file_set_external_attributes.o \
    zip_file_set_mtime.o \
    zip_file_strerror.o \
    zip_fopen.o \
    zip_fopen_encrypted.o \
    zip_fopen_index.o \
    zip_fopen_index_encrypted.o \
    zip_fread.o \
    zip_fseek.o \
    zip_ftell.o \
    zip_get_archive_comment.o \
    zip_get_archive_flag.o \
    zip_get_encryption_implementation.o \
    zip_get_file_comment.o \
    zip_get_name.o \
    zip_get_num_entries.o \
    zip_get_num_files.o \
    zip_hash.o \
    zip_io_util.o \
    zip_libzip_version.o \
    zip_memdup.o \
    zip_mkstempm.o \
    zip_name_locate.o \
    zip_new.o \
    zip_open.o \
    zip_progress.o \
    zip_random_unix.o \
    zip_rename.o \
    zip_replace.o \
    zip_set_archive_comment.o \
    zip_set_archive_flag.o \
    zip_set_default_password.o \
    zip_set_file_comment.o \
    zip_set_file_compression.o \
    zip_set_name.o \
    zip_source_accept_empty.o \
    zip_source_begin_write.o \
    zip_source_begin_write_cloning.o \
    zip_source_buffer.o \
    zip_source_call.o \
    zip_source_close.o \
    zip_source_commit_write.o \
    zip_source_compress.o \
    zip_source_crc.o \
    zip_source_error.o \
    zip_source_file.o \
    zip_source_filep.o \
    zip_source_free.o \
    zip_source_function.o \
    zip_source_get_compression_flags.o \
    zip_source_is_deleted.o \
    zip_source_layered.o \
    zip_source_open.o \
    zip_source_pkware.o \
    zip_source_read.o \
    zip_source_remove.o \
    zip_source_rollback_write.o \
    zip_source_seek.o \
    zip_source_seek_write.o \
    zip_source_stat.o \
    zip_source_supports.o \
    zip_source_tell.o \
    zip_source_tell_write.o \
    zip_source_window.o \
    zip_source_write.o \
    zip_source_zip.o \
    zip_source_zip_new.o \
    zip_stat.o \
    zip_stat_index.o \
    zip_stat_init.o \
    zip_strerror.o \
    zip_string.o \
    zip_unchange_all.o \
    zip_unchange_archive.o \
    zip_unchange.o \
    zip_unchange_data.o \
    zip_utf-8.o \

#    zip_source_winzip_aes_decode.o \
#    zip_source_winzip_aes_encode.o \
#    zip_winzip_aes.o \

%.o : %.c
	$(CC) -c $(CFLAGS) $*.c 

zip_add.o: zip_add.c $(HEADERS)
zip_add_dir.o: zip_add_dir.c $(HEADERS)
zip_add_entry.o: zip_add_entry.c $(HEADERS)
zip_algorithm_bzip2.o: zip_algorithm_bzip2.c $(HEADERS)
zip_algorithm_deflate.o: zip_algorithm_deflate.c $(HEADERS)
zip_algorithm_xz.o: zip_algorithm_xz.c $(HEADERS)
zip_buffer.o: zip_buffer.c $(HEADERS)
zip_close.o: zip_close.c $(HEADERS)
zip_crypto_openssl.o: zip_crypto_openssl.c $(HEADERS)
zip_delete.o: zip_delete.c $(HEADERS)
zip_dir_add.o: zip_dir_add.c $(HEADERS)
zip_dirent.o: zip_dirent.c $(HEADERS)
zip_discard.o: zip_discard.c $(HEADERS)
zip_entry.o: zip_entry.c $(HEADERS)
zip_error.o: zip_error.c $(HEADERS)
zip_error_clear.o: zip_error_clear.c $(HEADERS)
zip_error_get.o: zip_error_get.c $(HEADERS)
zip_error_get_sys_type.o: zip_error_get_sys_type.c $(HEADERS)
zip_error_strerror.o: zip_error_strerror.c $(HEADERS)
zip_error_to_str.o: zip_error_to_str.c $(HEADERS)
zip_err_str.o: zip_err_str.c $(HEADERS)
zip_extra_field_api.o: zip_extra_field_api.c $(HEADERS)
zip_extra_field.o: zip_extra_field.c $(HEADERS)
zip_fclose.o: zip_fclose.c $(HEADERS)
zip_fdopen.o: zip_fdopen.c $(HEADERS)
zip_file_add.o: zip_file_add.c $(HEADERS)
zip_file_error_clear.o: zip_file_error_clear.c $(HEADERS)
zip_file_error_get.o: zip_file_error_get.c $(HEADERS)
zip_file_get_comment.o: zip_file_get_comment.c $(HEADERS)
zip_file_get_external_attributes.o: zip_file_get_external_attributes.c $(HEADERS)
zip_file_get_offset.o: zip_file_get_offset.c $(HEADERS)
zip_filerange_crc.o: zip_filerange_crc.c $(HEADERS)
zip_file_rename.o: zip_file_rename.c $(HEADERS)
zip_file_replace.o: zip_file_replace.c $(HEADERS)
zip_file_set_comment.o: zip_file_set_comment.c $(HEADERS)
zip_file_set_encryption.o: zip_file_set_encryption.c $(HEADERS)
zip_file_set_external_attributes.o: zip_file_set_external_attributes.c $(HEADERS)
zip_file_set_mtime.o: zip_file_set_mtime.c $(HEADERS)
zip_file_strerror.o: zip_file_strerror.c $(HEADERS)
zip_fopen.o: zip_fopen.c $(HEADERS)
zip_fopen_encrypted.o: zip_fopen_encrypted.c $(HEADERS)
zip_fopen_index.o: zip_fopen_index.c $(HEADERS)
zip_fopen_index_encrypted.o: zip_fopen_index_encrypted.c $(HEADERS)
zip_fread.o: zip_fread.c $(HEADERS)
zip_fseek.o: zip_fseek.c $(HEADERS)
zip_ftell.o: zip_ftell.c $(HEADERS)
zip_get_archive_comment.o: zip_get_archive_comment.c $(HEADERS)
zip_get_archive_flag.o: zip_get_archive_flag.c $(HEADERS)
zip_get_encryption_implementation.o: zip_get_encryption_implementation.c $(HEADERS)
zip_get_file_comment.o: zip_get_file_comment.c $(HEADERS)
zip_get_name.o: zip_get_name.c $(HEADERS)
zip_get_num_entries.o: zip_get_num_entries.c $(HEADERS)
zip_get_num_files.o: zip_get_num_files.c $(HEADERS)
zip_hash.o: zip_hash.c $(HEADERS)
zip_io_util.o: zip_io_util.c $(HEADERS)
zip_libzip_version.o: zip_libzip_version.c $(HEADERS)
zip_memdup.o: zip_memdup.c $(HEADERS)
zip_mkstempm.o: zip_mkstempm.c $(HEADERS)
zip_name_locate.o: zip_name_locate.c $(HEADERS)
zip_new.o: zip_new.c $(HEADERS)
zip_open.o: zip_open.c $(HEADERS)
zip_progress.o: zip_progress.c $(HEADERS)
zip_random_unix.o: zip_random_unix.c $(HEADERS)
zip_rename.o: zip_rename.c $(HEADERS)
zip_replace.o: zip_replace.c $(HEADERS)
zip_set_archive_comment.o: zip_set_archive_comment.c $(HEADERS)
zip_set_archive_flag.o: zip_set_archive_flag.c $(HEADERS)
zip_set_default_password.o: zip_set_default_password.c $(HEADERS)
zip_set_file_comment.o: zip_set_file_comment.c $(HEADERS)
zip_set_file_compression.o: zip_set_file_compression.c $(HEADERS)
zip_set_name.o: zip_set_name.c $(HEADERS)
zip_source_accept_empty.o: zip_source_accept_empty.c $(HEADERS)
zip_source_begin_write.o: zip_source_begin_write.c $(HEADERS)
zip_source_begin_write_cloning.o: zip_source_begin_write_cloning.c $(HEADERS)
zip_source_buffer.o: zip_source_buffer.c $(HEADERS)
zip_source_call.o: zip_source_call.c $(HEADERS)
zip_source_close.o: zip_source_close.c $(HEADERS)
zip_source_commit_write.o: zip_source_commit_write.c $(HEADERS)
zip_source_compress.o: zip_source_compress.c $(HEADERS)
zip_source_crc.o: zip_source_crc.c $(HEADERS)
zip_source_error.o: zip_source_error.c $(HEADERS)
zip_source_file.o: zip_source_file.c $(HEADERS)
zip_source_filep.o: zip_source_filep.c $(HEADERS)
zip_source_free.o: zip_source_free.c $(HEADERS)
zip_source_function.o: zip_source_function.c $(HEADERS)
zip_source_get_compression_flags.o: zip_source_get_compression_flags.c $(HEADERS)
zip_source_is_deleted.o: zip_source_is_deleted.c $(HEADERS)
zip_source_layered.o: zip_source_layered.c $(HEADERS)
zip_source_open.o: zip_source_open.c $(HEADERS)
zip_source_pkware.o: zip_source_pkware.c $(HEADERS)
zip_source_read.o: zip_source_read.c $(HEADERS)
zip_source_remove.o: zip_source_remove.c $(HEADERS)
zip_source_rollback_write.o: zip_source_rollback_write.c $(HEADERS)
zip_source_seek.o: zip_source_seek.c $(HEADERS)
zip_source_seek_write.o: zip_source_seek_write.c $(HEADERS)
zip_source_stat.o: zip_source_stat.c $(HEADERS)
zip_source_supports.o: zip_source_supports.c $(HEADERS)
zip_source_tell.o: zip_source_tell.c $(HEADERS)
zip_source_tell_write.o: zip_source_tell_write.c $(HEADERS)
zip_source_window.o: zip_source_window.c $(HEADERS)
zip_source_winzip_aes_decode.o: zip_source_winzip_aes_decode.c $(HEADERS)
zip_source_winzip_aes_encode.o: zip_source_winzip_aes_encode.c $(HEADERS)
zip_source_write.o: zip_source_write.c $(HEADERS)
zip_source_zip.o: zip_source_zip.c $(HEADERS)
zip_source_zip_new.o: zip_source_zip_new.c $(HEADERS)
zip_stat.o: zip_stat.c $(HEADERS)
zip_stat_index.o: zip_stat_index.c $(HEADERS)
zip_stat_init.o: zip_stat_init.c $(HEADERS)
zip_strerror.o: zip_strerror.c $(HEADERS)
zip_string.o: zip_string.c $(HEADERS)
zip_unchange_all.o: zip_unchange_all.c $(HEADERS)
zip_unchange_archive.o: zip_unchange_archive.c $(HEADERS)
zip_unchange.o: zip_unchange.c $(HEADERS)
zip_unchange_data.o: zip_unchange_data.c $(HEADERS)
zip_utf-8.o: zip_utf-8.c $(HEADERS)
zip_winzip_aes.o: zip_winzip_aes.c $(HEADERS)

clean:
	rm -f *.o
	rm -f *.so

libzip.so: $(OBJS)
#	$(LD) -o libzip.so $(OBJS) $(LDFLAGS)
	$(CC) -shared -o libzip.so $(OBJS) $(LDFLAGS)

all: libzip.so

