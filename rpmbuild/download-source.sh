#!/bin/sh

src="lepton-eda-1.9.13.tar.gz"
url="https://github.com/lepton-eda/lepton-eda/releases/download/1.9.13-20201211/${src}"
out="SOURCES/${src}"

wget -c $url -O $out

