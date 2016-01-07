package html

import (
    // . "ml/dict"
    . "ml/array"
    . "ml/strings"
    . "ml/trace"

    "github.com/PuerkitoBio/goquery"
)

type Html struct {
    *goquery.Document
}

func Parse(html String) *Html {
    doc, err := goquery.NewDocumentFromReader(html.NewReader())
    RaiseIf(err)
    return &Html{
        Document: doc,
    }
}

func (self *Html) GetAllElements(ids Array) map[string]*goquery.Selection {
    data := map[string]*goquery.Selection{}

    self.Find("[id]").Each(func(i int, s *goquery.Selection) {
        i, exist := ids.Index(s.Attr2("id"))
        if exist {
            data[ids[i].(string)] = s
        }
    })

    return data
}
