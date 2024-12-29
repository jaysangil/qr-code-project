# Use the official Node.js image as the base
FROM node:18-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy the package files and install dependencies
COPY package.json yarn.lock ./
RUN yarn install

# Copy the rest of the application files
COPY . .

# Build the Next.js app
RUN yarn build

# Expose the port on which the frontend will run
EXPOSE 3000

# Start the Next.js app
CMD ["yarn", "start"]

