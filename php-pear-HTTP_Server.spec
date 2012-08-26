%define		_status		alpha
%define		_pearname	HTTP_Server
%include	/usr/lib/rpm/macros.php
Summary:	%{_pearname} - HTTP server class
Summary(pl.UTF-8):	%{_pearname} - klasa do obsługi serwera HTTP
Name:		php-pear-%{_pearname}
Version:	0.4.1
Release:	2
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	05b23509d6d9c34a2b78837a272218e5
URL:		http://pear.php.net/package/HTTP_Server/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(core) >= 4.2.0
Requires:	php-pear
Requires:	php-pear-HTTP
Requires:	php-pear-Net_Server >= 0.12.0
Requires:	php-pear-PEAR-core
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
%{_pearname} class that allows you to easily implement HTTP servers by
supplying callbacks. The base class will parse the request, call the
apropriate callback and build a response based on an array that the
callbacks have to return.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Klasa HTTP_Server pozwala na łatwe implementowanie serwerów HTTP
poprzez dostarczanie callbacków. Klasa bazowa analizuje żądanie,
wywołuje odpowiedni callback i tworzy odpowiedź w oparciu o tablicę
zwróconą przez callback.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/examples
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/HTTP/*.php
%{php_pear_dir}/HTTP/Server
