#include <iostream>
#include <thread>
#include <string>
#include <string_view>
#include <vector>

/*
 * @summary: This function splits a string into a vector of strings, using a delimiter.
 * @param: std::string_view str - The string to split, as a string_view; note you can pass a string, and it will
 * implicitly cast it to string_view.
 * @param: char delimiter - The delimiter character to split the string by.
 * @return: std::vector<std::string> - A vector of strings, containing the split string.
 */
std::vector<std::string_view> split_string(std::string_view str, char delimiter)
{
    std::vector<std::string_view> result;
    size_t size = 0;

    // points to start of the string, or current substring
    const char* start = str.data();

    // for each character in the string
    for (const char c : str)
    {
        // if the character is the delimiter
        if (c == delimiter)
        {
            // add the string from the start to the current character to the result
            result.emplace_back(start, size);
            // set the start pointer to the next character
            start += size + 1;
            // reset the size
            size = 0;
            continue;
        }

        // if the character is not the delimiter, increment the size and continue
        size++;
    }

    // add the last string to the result, if there is one
    if (size) result.emplace_back(start, size);
    // return the resultant vector containing the strings.
    return result;
}
