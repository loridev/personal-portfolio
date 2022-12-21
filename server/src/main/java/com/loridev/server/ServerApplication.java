package com.loridev.server;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.HashMap;

@SpringBootApplication
@RestController
public class ServerApplication {

	public static void main(String[] args) {
		SpringApplication.run(ServerApplication.class, args);
	}

	@GetMapping("/")
	public HashMap<String, Object> sayHello(@RequestParam(value = "myName", defaultValue = "World") String name) {
		HashMap<String, Object> response = new HashMap<>();
		response.put("status", 200);
		response.put("message", String.format("Hello %s", name));
		return response;
	}

}
