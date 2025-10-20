import { Blockquote, Center } from "@chakra-ui/react";

const Quote = ({ quote, author }) => {
  const authorName = author || "author";
  const quoteString = quote || "An inspirational quote";
  return (
    <Center pb="32px">
      <Blockquote.Root>
        <Blockquote.Content cite={authorName}>{quoteString}</Blockquote.Content>
        <Blockquote.Caption pl="20px">
          -- <cite>{authorName}</cite>
        </Blockquote.Caption>
      </Blockquote.Root>
    </Center>
  );
};

export { Quote };
