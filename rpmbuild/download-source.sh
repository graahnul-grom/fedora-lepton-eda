#!/bin/sh

src="lepton-eda-1.9.11.tar.gz"
url="https://github.com/lepton-eda/lepton-eda/releases/download/1.9.11-20200604/${src}"
out="SOURCES/${src}"

wget -c $url -O $out

