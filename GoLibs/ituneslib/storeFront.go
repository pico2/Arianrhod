package ituneslib

type CountryID int

const (
    CountryID_China       = CountryID(143465)
    CountryID_India       = CountryID(143467)
    CountryID_NewZealand  = CountryID(143461)
    CountryID_Vietnam     = CountryID(143471)
)

var storeFront = map[CountryID]string{
    CountryID_China         : "143465-19,32",
    CountryID_India         : "143467,32",
    CountryID_NewZealand    : "143461,32",
    CountryID_Vietnam       : "143471-2,32",
}

var countryShortName = map[CountryID]string{
    CountryID_China         : "CN",
    CountryID_India         : "IN",
    CountryID_NewZealand    : "NZ",
    CountryID_Vietnam       : "VN",
}

var countryName = map[CountryID]string{
    CountryID_China         : "China",
    CountryID_India         : "India",
    CountryID_NewZealand    : "NewZealand",
    CountryID_Vietnam       : "Vietnam",
}

func (self CountryID) String() string {
    return countryName[self]
}

func (self CountryID) ShortName() string {
    return countryShortName[self]
}

func (self CountryID) CountryCode() int {
    return int(self)
}

func (self CountryID) StoreFront() string {
    return storeFront[self]
}
