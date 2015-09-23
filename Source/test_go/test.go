package main

import (
    . "fmt"
    . "ml/strings"
    "encoding/json"
    "./pinyin"
    "ml/random"
    "os"
    "io/ioutil"
    "regexp"
)

func genacc() {
    py := [][]string{}
    json.Unmarshal([]byte(pinyin.Json), &py)

    f, _ := os.Open("domains.txt")
    bytes, _ := ioutil.ReadAll(f)
    f.Close()

    domains := String(bytes).SplitLines()

    // names := []string{}
    nameset := map[string]bool{}

    target  := 500000
    perline := 30000
    index   := 0

    names := []String{}

    for i := 0; i != target; i++ {
        name := ""
        for n := random.IntRange(1, 5); n > 0; {
            p := py[random.ChoiceIndex(py)][1]
            if len(p) > 4 {
                continue
            }

            name += p
            n--
        }

        name += Sprintf("%d@%s", random.IntRange(1000, 100000), random.Choice(domains).(String))
        if nameset[name] {
            i--
            continue
        }

        nameset[name] = true
        names = append(names, String(name))

        switch {
            case i + 1 == target,
                 i != 0 && i % perline == 0:
                 f, _ = os.Create(Sprintf("names%d.txt", index))
                 f.WriteString("INSERT IGNORE INTO appstore_buydata_appleid (username) VALUES (\"")
                 f.WriteString(string(String("\"),(\"").Join(names)))
                 f.WriteString("\");\n")

                 f.Close()

                 index++
                 names = []String{}
        }
    }
}

var (
    FORM_DATA_PATTERN       = regexp.MustCompile(`"fd"\s*:\s*({.*?})`)
    WIDGET_KEY_PATTERN      = regexp.MustCompile(`"wk"\s*:\s*({.*?})`)
    STRIP_CALLBACK_PATTERN  = regexp.MustCompile(`.*\(({.*?})\).*`)
)

func peekProperty(text, property string) (value string) {
    pattern := regexp.MustCompile(Sprintf(`(?m:\.%s\s*=\s*(.*);?$)`, property))
    value = pattern.FindStringSubmatch(text)[1]
    return
}

func main() {
    text := `
        var iTSMetricsCallbackFunction = function() {
            ITSMetrics.reportingSuite = "appleitmswww,appleitmscn";
            ITSMetrics.omniture = ITSMetrics.createBaselineOmnitureObject();

            ITSMetrics.isPageMetricsEnabled = true;

            ITSMetrics.isBuyMetricsEnabled = true;


            /* Page Metrics */
            ITSMetrics.omniture.pageName = "Signup View Terms-CN";
            ITSMetrics.omniture.channel = "Signup";
            ITSMetrics.omniture.prop22 = "HTML";
            ITSMetrics.omniture.eVar22 = "HTML";
    `

    Println(peekProperty(text, "reportingSuite"))
    Println(peekProperty(text, "pageName"))
    Println(peekProperty(text, "channel"))
    Println(peekProperty(text, "prop22"))
    Println(peekProperty(text, "eVar22"))
}
