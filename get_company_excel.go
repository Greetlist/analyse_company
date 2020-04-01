package main

import (
    "fmt"
    "net/http"
    "io/ioutil"
    "strconv"
)

const (
    CASH_SHEET  = 1
    DEBT_SHEET  = 2
    PROFIT_SHEET = 3
)
var SHEET_NAME_MAP map[int]string = nil

func init() {
    SHEET_NAME_MAP = make(map[int]string)
    SHEET_NAME_MAP[CASH_SHEET] = "xjllb"
    SHEET_NAME_MAP[DEBT_SHEET] = "zcfzb"
    SHEET_NAME_MAP[PROFIT_SHEET] = "lrb"
}

func finish_request(res *http.Response, control_channel chan int) {
    if err := res.Body.Close(); err != nil {
        fmt.Printf("Close Body Error is : %v.\n", err)
    }
    <-control_channel
}

var trans http.Transport = http.Transport {
    DisableKeepAlives : true,
}

func download_company_files(sheet_type, last_company_code string, control_channel chan int) error {
    cur_url :=  fmt.Sprintf("http://quotes.money.163.com/service/%s_%s.html", sheet_type, last_company_code)
    client := http.Client {
        Transport : &trans,
    }
    res, err := client.Get(cur_url)
    if err != nil {
        fmt.Printf("Get Error is : %v.\n", err)
        return err
    }
    defer finish_request(res, control_channel)
    if res.StatusCode == 200 {
        data, _ := ioutil.ReadAll(res.Body)
        file_name := fmt.Sprintf("%s_csvs/%s_%s.csv", sheet_type, sheet_type, last_company_code)
        ioutil.WriteFile(file_name, data, 0644)
        fmt.Printf("The %s_%s Company download finish.\n", sheet_type, last_company_code)
    } else {
        fmt.Printf("The %s_%s Company is not exist.\n", sheet_type, last_company_code)
    }
    return nil
}

func main() {
    control_channel := make(chan int, 100)
    for code := 0; code < 1000000; code++ {
        suffix := strconv.Itoa(code)
        lack := 6 - len(suffix)
        var prefix string
        for i := 0; i < lack; i++ {
            prefix += "0"
        }
        last_company_code := prefix + suffix
        for _, type_string := range SHEET_NAME_MAP {
            control_channel <- 1
            go download_company_files(type_string, last_company_code, control_channel)
        }
    }
}
