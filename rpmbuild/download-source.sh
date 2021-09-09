#!/bin/sh

src="lepton-eda-1.9.16.tar.gz"
url="https://github.com/lepton-eda/lepton-eda/releases/download/1.9.16-20210731/${src}"
out="SOURCES/${src}"

wget -c $url -O $out

