#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-ipred
Version  : 0.9.14
Release  : 57
URL      : https://cran.r-project.org/src/contrib/ipred_0.9-14.tar.gz
Source0  : https://cran.r-project.org/src/contrib/ipred_0.9-14.tar.gz
Summary  : Improved Predictors
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: R-ipred-lib = %{version}-%{release}
Requires: R-ipred-license = %{version}-%{release}
Requires: R-prodlim
BuildRequires : R-TH.data
BuildRequires : R-mlbench
BuildRequires : R-prodlim
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
bagging for classification, regression and survival problems 
  as well as resampling based estimators of prediction error.

%package lib
Summary: lib components for the R-ipred package.
Group: Libraries
Requires: R-ipred-license = %{version}-%{release}

%description lib
lib components for the R-ipred package.


%package license
Summary: license components for the R-ipred package.
Group: Default

%description license
license components for the R-ipred package.


%prep
%setup -q -n ipred
cd %{_builddir}/ipred

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1678469754

%install
export SOURCE_DATE_EPOCH=1678469754
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/R-ipred
cp %{_builddir}/ipred/inst/COPYRIGHTS %{buildroot}/usr/share/package-licenses/R-ipred/31f0bd39fbabce49169d78b8c65483e2bfc00d87 || :
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/ipred/COPYRIGHTS
/usr/lib64/R/library/ipred/DESCRIPTION
/usr/lib64/R/library/ipred/INDEX
/usr/lib64/R/library/ipred/Meta/Rd.rds
/usr/lib64/R/library/ipred/Meta/data.rds
/usr/lib64/R/library/ipred/Meta/features.rds
/usr/lib64/R/library/ipred/Meta/hsearch.rds
/usr/lib64/R/library/ipred/Meta/links.rds
/usr/lib64/R/library/ipred/Meta/nsInfo.rds
/usr/lib64/R/library/ipred/Meta/package.rds
/usr/lib64/R/library/ipred/Meta/vignette.rds
/usr/lib64/R/library/ipred/NAMESPACE
/usr/lib64/R/library/ipred/NEWS
/usr/lib64/R/library/ipred/R/ipred
/usr/lib64/R/library/ipred/R/ipred.rdb
/usr/lib64/R/library/ipred/R/ipred.rdx
/usr/lib64/R/library/ipred/data/DLBCL.rda
/usr/lib64/R/library/ipred/data/GlaucomaMVF.rda
/usr/lib64/R/library/ipred/data/Smoking.rda
/usr/lib64/R/library/ipred/data/dystrophy.rda
/usr/lib64/R/library/ipred/doc/index.html
/usr/lib64/R/library/ipred/doc/ipred-examples.R
/usr/lib64/R/library/ipred/doc/ipred-examples.Rnw
/usr/lib64/R/library/ipred/doc/ipred-examples.pdf
/usr/lib64/R/library/ipred/help/AnIndex
/usr/lib64/R/library/ipred/help/aliases.rds
/usr/lib64/R/library/ipred/help/ipred.rdb
/usr/lib64/R/library/ipred/help/ipred.rdx
/usr/lib64/R/library/ipred/help/paths.rds
/usr/lib64/R/library/ipred/html/00Index.html
/usr/lib64/R/library/ipred/html/R.css
/usr/lib64/R/library/ipred/tests/ipred-bugs.R
/usr/lib64/R/library/ipred/tests/ipred-bugs.Rout.save
/usr/lib64/R/library/ipred/tests/ipred-segfault.R
/usr/lib64/R/library/ipred/tests/ipred-smalltest.R
/usr/lib64/R/library/ipred/tests/ipred-smalltest.Rout.save

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/ipred/libs/ipred.so
/usr/lib64/R/library/ipred/libs/ipred.so.avx2
/usr/lib64/R/library/ipred/libs/ipred.so.avx512

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/R-ipred/31f0bd39fbabce49169d78b8c65483e2bfc00d87
