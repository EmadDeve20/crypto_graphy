#include<stdio.h>
#include<ctype.h>

char alphabet[] = "abcdefghijklmnopqrstuvwxyz";

void lower(char *ptr){
	while(*ptr != '\0'){
		*ptr = tolower(*ptr);
		ptr++;
	}

}

void crypto(){
	char message[5];
	char secret[100] = "";
	int key;
	printf("Enter Your message: ");
	scanf("%s" , message);
	lower(message);
	printf("Enter Your key(1-26): ");
	scanf("%d" , &key);
	for(int i = 0; i < sizeof(message) / sizeof(message[0]) ; i++)
		for(int j = 0; j < sizeof(alphabet) / sizeof(alphabet[0]) ; j++)
			if(message[i] == alphabet[j] && j+key < 26)
				secret[i] += alphabet[j+key];
			else if(message[i] == alphabet[j] && j+key >= 26)
				secret[i] += alphabet[j+key-26];

	printf("This is your secret message: %s" , secret);


}

void uncrypto(){
	char text[100];
	char message[100]="";
	int key;
	printf("Enter Your text: ");
	scanf("%s" , message);
	printf("Enter Your key(1-26): ");
	scanf("%d" , &key);
	for(int i = 0; i < sizeof(text) / sizeof(text[0]) ; i++)
		for(int j = 0; j < sizeof(alphabet) / sizeof(alphabet[0]) ; j++)
			if(text[i] == alphabet[j])
				message[i] += alphabet[j-key];

	printf("This is your message: %s" , message);
}

int main(){

	printf("%s\n",alphabet);
	printf("Enter Your mode:\n1 - hide message(default)\n2 - Break the secret message\n");
	short choice;
	printf("choice: ");
	scanf("%hd" , &choice);

	if(choice == 1)
		crypto();
	else if(choice == 2)
		uncrypto();
	else
		printf("exitting!");
}


