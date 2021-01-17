# symbioinfo

## Introduction

The rest of this document introduces some RPM mischief in about four parts. All
of the commands below are intended to be run from the shell. This workflow has
only been tested on the following platforms

* Raspberry pi (8Gb) running [fedora 33 (aarch)](https://download.fedoraproject.org/pub/fedora/linux/releases/33/Server/armhfp/images/Fedora-Server-armhfp-33-1.2-sda.raw.xz)

## 1. Setup, configuration and installation

This workflow is based on the `symbioinfo` development version hosted at 
[sagrudd/symbioinfo](https://github.com/sagrudd/symbioinfo). If you are reading
this and you are not `@sagrudd` then I am expecting that you are using a `fork`
of the original project - first step let's define an environment variable; edit
the location if you're not me ...

```
 $ export SYMBIOINFO=sagrudd/symbioinfo
   # recommended to append to .profile - check that shell == bash
 $ ps -p $$
 $ vim .bash_profile
   ...
```

```
sudo yum install rpm-build libgit2-devel libcurl-devel openssl icu zlib-devel \
    libpng-devel freetype bzip2-devel libjpeg-turbo libsodium-devel \
    xclip libpq-devel pandoc
git clone https://github.com/$SYMBIOINFO rpmbuild

```

By convention, the `rpmbuild` working directory is located at `~/rpmbuild`. A
configuration file for the `rpmbuild` software is located at `~/.rpmmacros` -
you are welcome to stray from the documented path; the `PackYak` will be loading
the file path to use from this macro file ... 

## 2. Building a collection of RPMs using the PackYak

The [PackYak](https://github.com/sagrudd/packyak) can process installation
targets that include YAML format files and vectors of one or more package names.

A template installation targets file is included in the `github` repository that
was just downloaded; please review and edit the `rpm_targets.yaml` file. The
RPM collection to prepare will be parsed directly from this file.

A number of the R packages encountered during the build will have requirements
for packages that should be available on the system. There will be some pain
as the `PackYak` throws errors and dependencies need to be installed and ideally
the associated SPEC files should be manually updated ...

```
build_file <- system.file("extdata/rpm_targets.yaml", package="packyak")
Rscript -e 'packyak::PackYak$new(build_file, build_rpm=TRUE)'
```

## 3. Update and publish the repo

```
 rmarkdown::render_site()
```

## 4. Define the repo on a non build system

```

```
