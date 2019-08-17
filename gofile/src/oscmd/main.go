package main

import (
	"fmt"
	"os/exec"
)

func main() {

	cmdstr := "mv hello world"
	//cmdstr := "go version"
	cmd := exec.Command("bash", "-c", cmdstr)
	//or
	//cmd := exec.Command("go version")
	//cmd.Run()
	out, err := cmd.Output()
	if err != nil {
		fmt.Println("cmd err: ", err)
	} else {
		fmt.Println("cmd out: ", string(out))
	}

	//ioutil.ReadFile()
}

/*
func Cmd(cmd string, shell bool) []byte {
	if shell {
		out, err := exec.Command("bash", "-c", cmd).Output()
		if err != nil {
			panic("some error found")
		}
		return out
	} else {
		out, err := exec.Command(cmd).Output()
		if err != nil {
			panic("some error found")
		}
		return out
	}
}
func main() {
	//cmd := "ls -al"
	cmd := "python test.py"
	//cmd := "python -V" //没有输出
	//cmd := "env"
	out := string(Cmd(cmd, true))
	//out := string(Cmd(cmd,false))
	fmt.Println(out)
}
*/
