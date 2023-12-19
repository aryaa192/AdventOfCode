package main

import (
	"fmt"
	"flag"
	"strings"
	"unicode"
	"strconv"
	"io/ioutil"
	"log"
)

var inputFile = flag.String("inputFile", "inputs/day01.input", "Relative file path to use as input.")

func main() {
	flag.Parse()
	input := parseInput()
	fmt.Println(p1(input))
	fmt.Println(p2(input))
}

func p1(lines []string) int {
	sum := 0
	for _, line := range lines {
		sum += findNumber(line)
	}
	return sum
}

func p2(lines []string) int {
	sum := 0
	for _, line := range lines {
		sum += findNumber(convertSpelledDigitsToDigits(line))
	}
	return sum
}

func findNumber(line string) int {
	first := ""
	last := ""
	for _, char := range line {
		if unicode.IsDigit(char) {
			first = string(char) 

		}
	}
	runes := []rune(line)
	for i := len(runes) - 1; i >= 0; i-- {
		if unicode.IsDigit(runes[i]) {
			last = string(runes[i])
		}
	}
	num, _ := strconv.Atoi(last + first)
	return num
}

func convertSpelledDigitsToDigits(s string) string {
	digits := ""
	numAsWords := map[string]string{
		"one": "1",
		"two": "2",
		"three": "3",
		"four": "4",
		"five": "5",
		"six": "6",
		"seven": "7",
		"eight": "8",
		"nine": "9",
	}
	for i, c := range s {
		if c >= '1' && c <= '9' {
			digits += string(c)
		} else {
			for word, digit := range numAsWords {
				if strings.HasPrefix(s[i:], word) {
					digits += string(digit)
					break
				}
			}
		}
	}
	return digits
}


func parseInput() []string {
	b, err := ioutil.ReadFile(*inputFile)
	if err != nil {
		log.Fatal(err)
	}
	si := strings.Split(string(b), "\n")
	return si
}

