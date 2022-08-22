#!/bin/sh

src="lepton-eda-1.9.18.tar.gz"
url="https://github.com/lepton-eda/lepton-eda/releases/download/1.9.18-20220529/${src}"
out="SOURCES/${src}"

wget -c $url -O $out

