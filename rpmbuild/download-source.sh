#!/bin/sh

src="lepton-eda-1.9.15.tar.gz"
url="https://github.com/lepton-eda/lepton-eda/releases/download/1.9.15-20210626/${src}"
out="SOURCES/${src}"

wget -c $url -O $out

