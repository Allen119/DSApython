from typing import List

def divide_array(arr: List[int]) -> List[List[int]]:
    """
    Splits the input array into subarrays separated by zeros.
    """
    result = []
    current_subarray = []

    for element in arr:
        if element == 0:
            if current_subarray:
                result.append(current_subarray)
                current_subarray = []
        else:
            current_subarray.append(element)

    # Append the last subarray if there's any leftover
    if current_subarray:
        result.append(current_subarray)

    print("Divided Subarrays:", result)  # Debugging
    return result

def max_product_subarray(arr: List[int]) -> int:
    """
    Calculates the maximum product of all subarrays obtained from divide_array.
    """
    if len(arr) == 1:
        return arr[0]
    
    subarrays = divide_array(arr)
    max_product = float('-inf')  # Start with a very small number
    print("Number of Subarrays:", len(subarrays))  # Debugging

    for subarray in subarrays:
        total_product = 1
        negative_count = 0
        first_negative = None
        last_negative = None
        
        # Calculate the total product and identify first and last negative numbers
        for i, num in enumerate(subarray):
            total_product *= num
            if num < 0:
                negative_count += 1
                if first_negative is None:
                    first_negative = i
                last_negative = i

        print(f"Subarray: {subarray}, Total Product: {total_product}, Negative Count: {negative_count}")  # Debugging

        # If no negatives or an even number of negatives, use the full product
        if negative_count % 2 == 0:
            max_product = max(max_product, total_product)
        else:
            print(len(subarray))
            # Odd number of negatives: exclude either the first or the last negative
            if len(subarray) == 1:  # Special case: only one element in subarray
                product_without_first_neg = 0
                product_without_last_neg = 0
            else:
                product_without_first_neg = 1
                product_without_last_neg = 1

                # Exclude first negative
                for j in range(first_negative + 1, len(subarray)):
                    product_without_first_neg *= subarray[j]

                # Exclude last negative
                for j in range(0, last_negative):
                    product_without_last_neg *= subarray[j]

            print("Product without first negative:", product_without_first_neg)  # Debugging
            print("Product without last negative:", product_without_last_neg)  # Debugging
            
            # Take the maximum between excluding first or last negative
            max_product = max(max_product, product_without_first_neg, product_without_last_neg)

    return max_product

# Example usage
arr = [2,4,2,4,-3,8,3,1]
print("Max Product Subarray:", max_product_subarray(arr))
