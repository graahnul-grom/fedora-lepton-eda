#!/bin/sh

if [ "${1}" = "-c" ]
then
    rpmlint --verbose SPECS/lepton-eda.spec
    if [ $? -ne 0 ]
    then
        echo -n " >> rpmlint errors. continue [y/N]? "
        read answ
        if [ "${answ}" != "y" ]
        then
            exit 1
        fi
    fi
fi

rpmbuild \
    --define="%_topdir `pwd`" \
    -ba \
    --nodebuginfo \
    SPECS/lepton-eda.spec \
    2>&1 | tee rpmbuild-ba.log

