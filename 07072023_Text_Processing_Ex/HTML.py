input_title_of_article = input()
input_content_of_article = input()

print(f"<h1>\n"
      f"\t{input_title_of_article}\n"
      f"</h1>")

print(f"<article>\n"
      f"\t{input_content_of_article}\n"
      f"</article>")

while True:
    command = input()
    if command == "end of comments":
        break

    print(f"<div>\n"
          f"\t{command}\n"
          f"</div>")

