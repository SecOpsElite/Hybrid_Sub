
package main

import (
    "fmt"
    "os/exec"
)

func runPassive(domain string) {
    fmt.Println("[+] Running passive enumeration...")
    exec.Command("subfinder", "-d", domain, "-silent", "-o", "passive.txt").Run()
    exec.Command("sh", "-c", fmt.Sprintf("assetfinder --subs-only %s >> passive.txt", domain)).Run()
}

func runActive(domain string) {
    fmt.Println("[+] Running active enumeration...")
    exec.Command("puredns", "bruteforce", "wordlists/dns.txt", domain, "-r", "resolvers.txt", "--wildcard-test").Run()
}

func main() {
    var domain string
    fmt.Print("Enter target domain: ")
    fmt.Scanln(&domain)
    runPassive(domain)
    runActive(domain)
    fmt.Println("[+] Enumeration completed.")
}
