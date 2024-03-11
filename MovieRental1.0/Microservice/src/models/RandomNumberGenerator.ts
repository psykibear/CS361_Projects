/**
 * A utility class for generating random numbers within a specified range.
 */
export class RandomNumberGenerator {
    /**
     * Generates a random number within the specified range.
     * @param min The minimum value of the range (inclusive). Default is 0.
     * @param max The maximum value of the range (inclusive). Default is 100.
     * @returns A random number within the specified range.
     */
    static generate(min = 0, max = 100) {
        return Math.floor(Math.random() * (max - min + 1)) + min;
    }
}
